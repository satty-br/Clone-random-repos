import argparse
from github import Github
from git import Repo
import os
import shutil
import time

def selective_copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            try:
                shutil.copytree(s, d, symlinks, ignore)
            except:
                time.sleep(1)
        else:
            shutil.copy2(s, d)

def main(options):
    # First, create a 'Github' instance using a personal access token
    g = Github(options.token)

    # Then, get the organization
    org = g.get_organization(options.org)

    # Now, get the list of repositories you want to clone
    repos = g.search_repositories(query=f'language:{options.content_type} is:public fork:false archived:false', order='desc')

    # For each repository in the list
    repo_num = 0
    os.makedirs('./repos', exist_ok=True)

    for repo in repos:
        repo_num += 1
        if repo_num > options.num_repos:
            print('Done!')
            break
        # Clone the repository
        new_folder = f'./repos/{repo.name}'
        try:
            Repo.clone_from(repo.clone_url, new_folder)
        except:
            continue
        old_folder = f'./repos/{repo.name}_old'
        try:
            os.rename(new_folder, old_folder)
        except:
            continue
        try:
            shutil.rmtree(os.path.join(old_folder, ".github"))
        except:
            time.sleep(1)
            try:
                shutil.rmtree(os.path.join(old_folder, ".github"))
            except:
                pass

        
        # Create a new repository in your organization
        try:
            new_repo = org.create_repo(repo.name)
        except:
            continue
        new_repo_git = Repo.clone_from(new_repo.clone_url, new_folder)
        selective_copytree(old_folder, new_folder)
        new_repo_git.git.add(A=True)
        new_repo_git.git.commit(m='Initial commit')
        try:

            new_repo_git.git.push('origin', 'main')

        except:
            continue
        print(f'Cloned {repo.name} repositorie')
        try:
            shutil.rmtree(old_folder)
        except:
            pass
        try:
            shutil.rmtree(new_folder)
        except:
            pass
        print(f'Cloned {repo_num} repositories')
    shutil.rmtree('./repos', ignore_errors=True, dirs_exist_ok=True, topdown=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create fake repositories for PoC testing"
    )
    parser.add_argument(
        "--num_repos",
        type=int,
        default=100,
        help="Number of repositories to create",
    )
    parser.add_argument(
        "--content_type",
        choices=["python", "javascript", "java"],
        default="java",
        help="Type of code to generate (python, javascript)",
    )
    parser.add_argument(
        "--token",
        type=str,
        default=os.environ.get("GITHUB_TOKEN"),
        help="Github token",
    )
    parser.add_argument(
        "--org",
        type=str,
        default="random-org",
        help="Github organization",
    )
    options = parser.parse_args()
    main(options)

