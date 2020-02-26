"""
Assignment 2 - Webscraper
Option 2
"""


from bs4 import BeautifulSoup
from prettytable import PrettyTable
import re
import requests


def get_company_data(web_site_url, num_result, output_file_name):

    curr_pretty_table = PrettyTable()
    curr_pretty_table.field_names = ["Iteration", "Name", "Purpose"]
    curr_output_file = open(output_file_name, "w")
    success_index = 0

    while success_index < num_result:
        page = requests.get(web_site_url)
        if page.status_code == 200:
            success_index += 1
            curr_soup = BeautifulSoup(page.text, "html.parser")
            for tag in curr_soup.find_all(
                "li", text=re.compile(".*Name:.*|.*Purpose:.*")
            ):
                name_search = re.match(".*Name:\s*(.*)$", tag.text)
                if name_search:
                    curr_name = "{group}".format(
                        groupNum=1,
                        start=name_search.start(1),
                        end=name_search.end(1),
                        group=name_search.group(1),
                    )
                else:
                    purpose_search = re.match(".*Purpose:\s*(.*)$", tag.text)
                    if purpose_search:
                        curr_purpose = "{group}".format(
                            groupNum=1,
                            start=purpose_search.start(1),
                            end=purpose_search.end(1),
                            group=purpose_search.group(1),
                        )

            curr_pretty_table.add_row([success_index, curr_name, curr_purpose])

    curr_output_file.write(str(curr_pretty_table))
    curr_output_file.close()


if __name__ == "__main__":
    get_company_data(
        "http://18.207.92.139:8000/random_company", 50, "output_file_Option_2.txt"
    )


"""

Comment

I have come up with two possible solutions of "Assignment 2 - Webscraper".
The first possible solution is identified by "Option 1" and is contained
in the file named "Assignment.2.Webscraper.Option.1".
The second possible solution is identified by "Option 2" and is contained
in the file named "Assignment.2.Webscraper.Option.2" (which is this file,
the file you are reading).

Option 2

The code contained in "Option 2" (therefore the code contained in this file)
is almost the same as the code contained in "Option 1" (contained in the
file named "Assignment.2.Webscraper.Option.1").
Therefore, the comment of the code contained in "Option 2" (therefore the
comment of the code contained in this file you are reading) can be found
in the file "Assignment.2.Webscraper.Option.1".

How does the code of "Option 2" differ from the code of "Option 1"?

The output of the code contained in "Option 1" is a file that contains
a table with two columns (the headers of the two columns are "Name" and
"Purpose"), while the output of the code of "Option 2" (the output of
the file you are reading) is a file that contains a table with three
columns (the headers of the table in this case are "Iteration", "Name"
and "Purpose").
Therefore, in the code of "Option 2" (the code of this file you are reading)
on line 16 I set "curr_pretty_table.field_names" equal to
"["Iteration", "Name", "Purpose"]"; in this case I included also "Iteration",
which is missing in the code of "Option 1".
In a similar way, on line 46 I also included "success_index" in the
brackets ("success_index" is not included on line 46 of the code of
"Option 1").
Lastly, I also named the file created by the code of "Option 2" as
"output_file_Option_2.txt" and therefore I included
"output_file_Option_2.txt" on line 54 (the file created by the code of
"Option 1", instead, is named "output_file_Option_1.txt").

As I also did for the code of "Option 1", also in this case I use blank
lines (where necessary) to separate specific lines of code so that
the code can be easily read and understood. Moreover, I also use the triple
quotes to include text (at the beginning for the title and here for the
comment).

In conclusion, I type "black" in the terminal followed by the path of the
file in ".py format" in order to format the whole code contained in the
file taken into consideration (basically the code of the file you are
reading).

As stated before, the file created by the code of "Option 2" (therefore
the fle created by the code contained in the file you are reading)
contains a table with three columns and the headers of these three columns
are "Iteration", "Name" and "Purpose"; in this way, it is easy to verify
that the file in question actually contains exactly the 50 names and the
50 purposes of the 50 companies taken into consideration.

I then upload this file, named "output_file_Option_2.txt" on the Discussion
Board in Canvas.

 """
