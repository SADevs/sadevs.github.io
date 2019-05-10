Title: How to add docs to this site
Date: 11-29-2018
Tags: how-to, docs
Slug: how-to-add-docs
Authors: Omar Quimbaya
Summary: A short tutorial of how to add your docs to this site and share your knowledge!


First of all, why would you want to do this? We are a group of developers who are active in our Slack group, but one of the main problems is that we have a lot of knowledge that we are not writing down in a more permanent place. When we share articles or advice on a technical topic, those messages will get lost with all of the other messages that people are sending as we are not paying for our Slack subscription. Therefore, in order to share our knowledge with people and show other cities that the developers in San Antonio are knowledgeable, collaborative, and willing to share their experience with the rest of the world, we are giving developers here an opportunity to share articles on their thoughts, experiences, and knowledge of how to use the technologies we use every day.

This is a good opportunity for you to contribute something to the community without that much effort! In order to do so, here is how you do it.

## Fork the repo!

Our site is a static site hosted somewhere out there on the Internet. Super mysterious. You can find the repository of our site here: [https://github.com/SADevs/sadevs.github.io](https://github.com/SADevs/sadevs.github.io). [Fork](https://help.github.com/en/articles/fork-a-repo) the website's repo and [clone](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository) it to your local machine. Below are quick steps to clone your fork, update all the submodules (important to get our theme pulled down), and add the main repo as an upstream (important for syncing your fork later): 

    git clone [your fork url]
    git submodule update --init
    git remote add upstream git@github.com:SADevs/sadevs.github.io.git

## Syncing your fork
If you've already forked the repo and want to sync it, [Github](https://help.github.com/en/articles/syncing-a-fork) offers some great documentation on doing it. If you cloned the repo following the above steps, you can follow the Github's documentation. If you didn't check out [these directions](https://help.github.com/en/articles/configuring-a-remote-for-a-fork) for adding the remote.

You'll need to sync your fork after any changes are made in the main repo (like your PR being merged!!)

## Pelican Power!
The site is powered by [Pelican](https://github.com/getpelican/pelican), which is a static site generator written in Python. If you have Python on your machine and you want to see what your article looks like on your local machine, install Pelican by typing in your terminal 

    pip install pipenv # if you don't have pipenv on your machine already
    pipenv install

You can learn more about [pipenv here](https://realpython.com/pipenv-guide/).

This will get the necessary packages to use this static site generator. To build and run the site locally, use the following commands:

    pipenv run pelican content -vvv -o output -s pelicanconf.py
    cd output
    python -m http.server

Open a browser and go to http://localhost:8000 to view the content. **Note that the links will link to the actual site instead of the locally generated site, so if you made changes and you are not seeing them, check the URL at the top to see where you are.**

### New Article Template
Copy this template to get you started into a new file with a relevant name of your article and ending with a markdown extension:

    Title: How to install Pelican
    Date: 11-29-2018
    Tags: how-to, docs
    Slug: how-to-install-pelican
    Authors: Omar Quimbaya
    Summary: A short tutorial on how to install Pelican

    # How to install Pelican

    <some text goes here>

        # code example
        print("hello world")

    ## Secondary Heading

    ### Tertiary Heading

    [Links for more information](https://blog.getpelican.com/)

## Making a PR

Once your document is done and you feel like you've said all you could about a topic, commit and push that to the `website` branch of your clone repository. Go to your repo and submit a pull request to add your changes to the site. Once an admin reviews your article and accepts the pull request, it will start CI that will publish the article to the site.

## Additional Questions

If you have any more questions or run into any issues, reach out in #website on Slack. 

Happy writing, and thank you for contributing to the SA Developers Group!
