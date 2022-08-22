Git
===

* Source: https://education.github.com/git-cheat-sheet-education.pdf

Setup
-----

.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - :code:`git config --global user.name “[firstname lastname]”`
     - set a name that is identifiable for credit when review version history
   * - :code:`git config --global user.email “[valid-email]”`
     - set an email address that will be associated with each history marker
   * - :code:`git config --global color.ui auto`
     - set automatic command line coloring for Git for easy reviewing

Initialisation
--------------

.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - :code:`git init`
     - initialize an existing directory as a Git repository
   * - :code:`git clone [url]`
     - retrieve an entire repository from a hosted location via URL
   * - :code:`git config --global color.ui auto`
     - set automatic command line coloring for Git for easy reviewing

Stage & Snapshot
----------------

.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - :code:`git status`
     - show modified files in working directory, staged for your next commit
   * - :code:`git add [file]`
     - add a file as it looks now to your next commit (stage)
   * - :code:`git reset [file]`
     - unstage a file while retaining the changes in working directory
   * - :code:`git diff`
     - diff of what is changed but not staged
   * - :code:`git diff --staged`
     - diff of what is staged but not yet committed
   * - :code:`git commit -m “[descriptive message]”`
     - commit your staged content as a new commit snapshot

Branch & Merge
--------------

.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - :code:`git branch`
     - list your branches. a * will appear next to the currently active branch
   * - :code:`git branch [branch-name]`
     - create a new branch at the current commit
   * - :code:`git checkout`
     - switch to another branch and check it out into your working directory
   * - :code:`git merge [branch]`
     - merge the specified branch’s history into the current one
   * - :code:`git log`
     - show all commits in the current branch’s history