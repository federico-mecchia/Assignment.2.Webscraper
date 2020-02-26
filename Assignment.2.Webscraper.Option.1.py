"""
Assignment 2 - Webscraper
Option 1
"""


from bs4 import BeautifulSoup
from prettytable import PrettyTable
import re
import requests


def get_company_data(web_site_url, num_result, output_file_name):

    curr_pretty_table = PrettyTable()
    curr_pretty_table.field_names = ["Name", "Purpose"]
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

            curr_pretty_table.add_row([curr_name, curr_purpose])

    curr_output_file.write(str(curr_pretty_table))
    curr_output_file.close()


if __name__ == "__main__":
    get_company_data(
        "http://18.207.92.139:8000/random_company", 50, "output_file_Option_1.txt"
    )


"""

Comment

I have come up with two possible solutions of "Assignment 2 - Webscraper".
The first possible solution is identified by "Option 1" and is contained
in the file named "Assignment.2.Webscraper.Option.1" (which is this
file, the file you are reading). The second possible solution is identified
by "Option 2" and is contained in the file named
"Assignment.2.Webscraper.Option.2".

Option 1

First I import "BeautifulSoup" from "bs4" and "PrettyTable" from "prettytable"
and then also "re" and "requests".
I then use "def()" to define the function, I name it "get_company_data" and I
also include the three arguments "web_site_url", "num_result" and
"output_file_name". In addition to this, I also set "curr_pretty_table" equal
to "PrettyTable()", I set "curr_pretty_table.field_names" equal to
"["Name", "Purpose"]" (in other words the file which will be created will
contain a table with two columns and the headers of these columns will be
"Name" and "Purpose"), I set "curr_output_file" equal to
"open(output_file_name, "w")" and lastly I also set the "success_index" equal
to 0.
I then create a "while loop" by including "success_index < num_result" and in
the next row I set "page" equal to "requests.get(web_site_url)" (I am
taking into consideration one of the three arguments of the function I
defined in the beginning). I then create an "if loop" (success is identified
by "status_code == 200"). At this point 1 is added to "success_index"
("success_index" was set equal to 0 in the beginning). I also set "curr_soup"
equal to "BeautifulSoup(page.text, "html.parser")".
Furthermore, I create also a "for loop" by including
"tag in curr_soup.find_all" and then I also include 
""li", text=re.compile(".*Name:.*|.*Purpose:.*")" inside the brackets. In
addition to this, I also set "name_search" equal to
"re.match(".*Name:\s*(.*)$", tag.text)".
Moreover, I create an "if else loop". First I take into consideration
"name_search" and I set "curr_name" equal to 
""{group}".format(groupNum=1,start=name_search.start(1),
end=name_search.end(1),group=name_search.group(1),)". I then take into
consideration "purpose_search", I set "purpose_search" equal to
"re.match(".*Purpose:\s*(.*)$", tag.text)" and I also set "curr_purpose"
equal to ""{group}".format(groupNum=1,start=purpose_search.start(1),
end=purpose_search.end(1),group=purpose_search.group(1),)".
Furthermore, I add a row to the table by using
"curr_pretty_table.add_row([curr_name, curr_purpose])".
I then include also "curr_output_file.write(str(curr_pretty_table))"
and "curr_output_file.close()" in the "while loop" I created in the
beginning.
Lastly, I use "if __name__ == "__main__":" and I include the three arguments
in the "get_company_data" function I created. More specifically, I include
in the brackets ""http://18.207.92.139:8000/random_company"", 50 (since I
want to obtain the 50 names and the 50 purposes of the 50 companies
taken into consideration) and "output_file_Option_1.txt"
(which is the name of the file created by the function "get_company_data").

I use blank lines (where necessary) to separate specific lines of code so that
the code can be easily read and understood. Moreover, I also use the triple
quotes to include text (at the beginning for the title and here for the
comment).

In conclusion, I type "black" in the terminal followed by the path of the
file in ".py format" in order to format the whole code contained in the
file taken into consideration (basically the code of the file you are
reading).

The file created in "Option 1" (named "output_file_Option_1.txt") contains
a table with two columns (the headers of the columns are "Name" and
"Purpose") and the 50 names and the 50 purposes of the 50 companies taken
into consideration.
I then upload this file, named "output_file_Option_1.txt" on the Discussion
Board in Canvas.

 """
