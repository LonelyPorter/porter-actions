# porter-actions
Porter's Github Actions library

## version-check
This is an action to check if your project version is updated before merging in PR

### How to use
Have a `project.toml` file in your repo  
File looks like:  
```toml
[Project]
  name = "xxx"
  version = "x.x.x"
```

Then put the following in your github actions workflow  
```yaml
- uses: actions/checkout@v3
  with:
    ref: ${{ github.event.pull_request.head.sha }}
    fetch-depth: 2
- uses: LonelyPorter/porter-actions/version-check@version
```
This will reference the last two commits in PR(branch) and compare the two to see if `project.toml` is being touched  

Basically, this requires you to version bump(change) at the newest commit before you do the merge in PR 

*TODO*:
* smarter version check
* multiple version check in one PR 


## More coming in the way