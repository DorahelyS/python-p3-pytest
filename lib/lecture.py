'''
Key Vocab
Unit Testing: a development process where the smallest testable parts of an application are independently tested 
for proper functionality.
Test-Driven Development: a development process where tests are written to meet expectations for an application 
before code is written to meet those expectations.
Assertion: a statement that determines if a wrapped statement produces a falsy value or exception. In either case, 
the assertion fails and the execution of code stops.
Flag: a method of providing options to modify commands from the command line. Flags begin with a dash -.

pytest is a testing framework in Python that makes it easy to write short, easy-to-parse tests for applications 
ranging from a single function to huge libraries.


Customizing pytest Output
When running commands from the command line, you often have the option to include flags. Flags are a way to modify your commands- they begin with a dash -, and they're tailored to each command they're used with. For example, cp (copy) has a -r flag that specifies that the copy operation should be recursive- you need to use this to copy a directory and its contents. tree has a -L flag that allows you to specify the depth of subdirectories you want to include in its output.

pytest has many flags, but we're just going to focus on the few that will be most helpful to you.

-x is pytest's "exit" flag. This executes tests until one fails, then stops executing tests. This is very helpful for test-driven development, as you'll want to focus on developing to one test at a time.
--pdb opens the Python debugger when a test fails. It does not open the prettier, improved ipdb, but its basic functions are very similar.
-s tells pytest to show the full output for failed tests (i.e. print() statements).
-q (for quiet) shortens pytest's output. Running with the -q flag will only show a single line for the summary of the testing session and details of the failures.
-h will help you figure out where to place arguments for the pytest command and provide a long list of flags and configurations for use with pytest.


'''