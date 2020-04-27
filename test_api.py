from github import Github


def test_get_current_user():

    # Github Enterprise with custom hostname
    access_token = 'token_here'
    g = Github(base_url="url_here", login_or_token=access_token)

    # get current user
    print(g.get_user().login)
    assert "user_here" == g.get_user().login

def test_get_user_by_name():
    access_token = 'token_here'
    g = Github(base_url="url_here", login_or_token=access_token)

    # get current user
    user = g.get_user("user_here")
    assert "user_here" == user.name



def test_get_organization():
    access_token = 'token_here'
    g = Github(base_url="url_here", login_or_token=access_token)
    org = g.get_organization("CoreTech-GRID")
    assert "CoreTech-GRID" == org.login

# https://stackoverflow.com/questions/34392221/api-calls-to-get-number-of-commits-by-author-github-api
def test_get_commits():
    access_token = 'token_here'
    g = Github(base_url="url_here", login_or_token=access_token)
    counter = 0
    for event in g.get_user("user_here").get_events():
        if event.type == "PushEvent":
            print(f"Type={event.type} date={event.created_at} project={event.repo.full_name}")
            counter+=1
    print(f"Total commits={counter}")


# https://www.thepythoncode.com/article/using-github-api-in-python
def test_get_commits_by_repo():
    access_token = 'token_here'
    g = Github(base_url="url_here", login_or_token=access_token)
    repo = g.get_repo("repo_here")
    assert "" == repo.get_commits().totalCount()
    # returned commits in a paginated list
    commits = repo.get_commits()

