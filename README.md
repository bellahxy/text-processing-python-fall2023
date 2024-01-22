[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/5TBgPbjp)
# Data Skills 2: Homework 2
### Text Processing

__Due Date: Monday, October 23rd by 11:59pm__
  
__Parsing PDF Tables__

The document 2005proposal.pdf is from the 2005 Base Realignment and Closure (BRAC) Commission.  This is a group that proposes military base changes in a process designed to insulate decisions from political interference.  Bases can be "realigned" - that is, gain or loose employment, they can be "closed" all together, or be unaffected.  The tables organize bases by which Metropolitan Statistical Area (Note that while MOST entries are MSAs, there are some others, including counties and metropolitan divisions. You can leave them all in under the header of "msas") they are a part of, followed by the proposed changes (details listed earlier in the document).  This document was originally parsed as part of an actual research project, so the goal for you is to practice on semi-structured text data with real applications.

The PDF document is included only for your reference - the file you will be working from is named 2005proposal.pdf.txt, and is the result of parsing the PDF document to extract text.  It did not come out completely clean, however.  Your task is to study the text output, compare it to the source PDF, then write a script that takes in the text document and outputs a CSV document.  See the included image DS2_Python_HW3_answer_sample.png for the desired format.

The only thing you need from this document are the tables, which in the PDF document begin on page 3, and end on page 48.  Remember to clean up any code you used to explore the data, but that isn't part of the final answer, e.g. intermediate print statements, df.head(), etc.

Your code does not need Pandas - instead, recall the structure of a CSV document as we've discussed in class, and build that directly using containers and strings.  It is ok to use regular expressions, though it is not required.  And finally, you do not need to use Spacy, or any other library besides os for that matter, to complete this task.

To begin, you will need to explore the text document in a text editor, side-by-side with the tables from the PDF document.  Get to know your starting point, and get familiar with the desired final result.  To start thinking about how to get from one to the other, you will need to identify unique types of line structures that show up repeatedly - in my version I found 6 that contain data.  You will be able to recieve most of the credit if you do well on the bulk of the document, even if you miss a few corner cases, so do not get too bogged down in making it perfect.  One logical approach is to think in terms of a loop that goes over each line, one at a time, applies the correct parsing, then a final loop over those parsed lines that assembles it all.  Good use of functions for organization and repetition will be crucial here, along with having a plan and using good comments.

In addition to a file named question2.py, include your final question2.csv file in the repo.  In the next assignment we will be connecting this data with some of what we created in homework 1 in order to analyze it.