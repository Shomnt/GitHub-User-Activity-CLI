import sys
import requests

def get_activity(username: str) -> dict:
    try:
        data = requests.get(f'https://api.github.com/users/{username}/events')
    except requests.exceptions.RequestException as e:
        print("Something went wrong")

    if data.status_code != 200:
        print(f'User with username {username} not found or user has no events')
        return

    return data.json()



def print_activity(data: dict) -> None:
    activity = dict()
    for event in data:
        if not activity.get(event["type"], False):
            activity[event["type"]] = dict()
        activity[event["type"]][event["repo"]["name"]] = activity[event["type"]].get(event["repo"]["name"], 0) + 1
    print(activity)

    for key in activity.keys():
        match key:
            case 'CommitCommentEvent':
                for rep, count in activity[key].items():
                    print(f'Commit {count} comments in {rep}')
            case 'CreateEvent':
                for rep, count in activity[key].items():
                    print(f'Create {count} branches or tags in {rep}')
            case 'DeleteEvent':
                for rep, count in activity[key].items():
                    print(f'Delete {count} branches or tags in {rep}')
            case 'ForkEvent':
                for rep, count in activity[key].items():
                    print(f'Fork {count} {rep}')
            case 'GollumEvent':
                for rep, count in activity[key].items():
                    print(f'Create or update {count} wiki pages in {rep}')
            case 'IssueCommentEvent':
                for rep, count in activity[key].items():
                    print(f'Create or update {count} issue comments in {rep}')
            case 'IssueEvent':
                for rep, count in activity[key].items():
                    print(f'Create or update {count} issue comments in {rep}')
            case 'MemberEvent':
                for rep, count in activity[key].items():
                    print(f'{count} collaborators in {rep}')
            case 'PublicEvent':
                for rep, count in activity[key].items():
                    print(f'Make {rep} is a public')
            case 'PullRequestEvent':
                for rep, count in activity[key].items():
                    print(f'{count} pull request in {rep}')
            case 'PullRequestReviewEvent':
                for rep, count in activity[key].items():
                    print(f'{count} pull request review in {rep}')
            case 'PullRequestReviewCommentEvent':
                for rep, count in activity[key].items():
                    print(f'{count} pull request review comment in {rep}')
            case 'PullRequestReviewThreadEvent':
                for rep, count in activity[key].items():
                    print(f'{count} pull request review thread in {rep}')
            case 'PushEvent':
                for rep, count in activity[key].items():
                    print(f'Pushed {count} comments to {rep}')
            case 'ReleaseEvent':
                for rep, count in activity[key].items():
                    print(f'Release {rep}')
            case 'SponsorshipEvent':
                for rep, count in activity[key].items():
                    print(f'{count} sponsorship listing in {rep}')
            case 'WatchEvent':
                for rep, count in activity[key].items():
                    print(f'Starred {rep}')


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) < 1:
        print("Usage: python main.py <username>")
        sys.exit(1)
    activity = get_activity(args[0])
    print_activity(activity)
