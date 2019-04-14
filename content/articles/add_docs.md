Title: How to add docs to this site
Date: 11-29-2018
Tags: how-to, docs
Slug: how-to-add-docs
Authors: Omar Quimbaya
Summary: A short tutorial of how to add your docs to this site and share your knowledge!

# How to add documentation to the SA Devs website

First of all, why would you want to do this? We are a group of developers who are active in our Slack group, but one of the main problems is that we have a lot of knowledge that we are not writing down in a more permanent place. When we share articles or advice on a technical topic, those messages will get lost with all of the other messages that people are sending as we are not paying for our Slack subscription. Therefore, in order to share our knowledge with people and show other cities that the developers in San Antonio are knowledgeable, collaborative, and willing to share their experience with the rest of the world, we are giving developers here an opportunity to share articles on their thoughts, experiences, and knowledge of how to use the technologies we use every day.

This is a good opportunity for you to contribute something to the community without that much effort! In order to do so, here is how you do it.

## Fork the repo!

Our site is a static site hosted somewhere out there on the Internet. Super mysterious. You can find the repository of our site here: [https://github.com/SADevs/sadevs.github.io](https://github.com/SADevs/sadevs.github.io). Fork this repository and clone it to your local machine. 

    git clone git@github.com:SADevs/sadevs.github.io.git
    git submodule update --init

The site is powered by Pelican, which is a static site generator written in Python. If you have Python on your machine and you want to see what your article looks like on your local machine, install Pelican by typing in your terminal 

    pip install -r requirements.txt

We recommend using a virtual environment to manage this project. You can use a couple of solutions to do that, such as virtualenv, pipenv, and pyenv. Whatever tool with which you are most comfortable. If you do not know what a virtual environment is, please read this article: [Python Virtual Environments, a Primer](https://realpython.com/python-virtual-environments-a-primer/).

This will get the necessary packages to use this static site generator. To build and run the site locally, use the following commands:

    make publish
    make serve

Open a browser and go to http://localhost:8000 to view the content. Note that the links will link to the actual site instead of the locally generated site, so if you made changes and you are not seeing them, check the URL at the top to see where you are.

If you don't care about what your article looks like on the site and just want to write content, copy this template to get you started into a new file with a relevant name of your article and ending with a markdown extension:

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

Once your document is done and you feel like you've said all you could about a topic, commit and push that to the `website` branch of your cloned repository. Go to your repo and submit a pull request to add your changes to the site. Once an admin reviews your article and accepts the pull request, it will publish the article to the site.

If you have any more questions or require additional details, please let @PropagandaPanda4 know on the Slack group. He can edit the article and add additional details.

Happy writing, and thank you for contributing to the SA Developers Group!
