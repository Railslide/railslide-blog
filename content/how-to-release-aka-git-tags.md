Title: How to release your code (aka Git tags)
Date: 2016-03-04
Category: /dev
Tags: git, github, release
Slug: how-to-release-aka-git-tabs
Author: Giulia Vergottini
Summary: After spending quite some time working on your side project, you feel that it is finally good enough for going public. Releasing sounds like a super neat idea, but how do you do it?
Status: draft

After spending quite some time working on your side project, you feel that it is finally good enough for going public. That's great, but now what? Releasing sounds like a super neat idea, but how do you do it?

As a matter of fact Github makes the process of releasing extremely simple. All you need to do is to click on the releases counter, press the _"Create a new release"_ button, fill the form, and submit. Refresh the main page of your repo and you'll see that the release counter has increased - congrats, you have just done your first release!

That's certainly awesome, but is it really neceessary to use the Github interface? Wouldn't it be possible to release directly from your trusted terminal? Of course it is possible, and it's also quite simple! In fact what Github does behind the scene is actually just setting a Git tag.

Tags in Git are a way to set a reference to a specific point in history. You can think of them as a way to _bookmark_ a specific commit. So when you download the source code for your-awesome-project.v1.1.0 you're basically saying "Hey Git, fetch me the code up to the point that corrispond to the commit tagged with the name your-awesome-project.v1.1.0".

