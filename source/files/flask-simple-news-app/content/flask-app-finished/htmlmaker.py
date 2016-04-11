from string import Template

MAIN_HTML = Template("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Congressional Birthdays</title>
</head>
<body>

<h1>On this date: ${date}</h1>
<h2>${member_count} Congressmember(s) have birthdays</h2>
<ul>
    ${list_html}
</ul>
</body>
</html
""")

LIST_ITEM_HTML = Template("""
   ${title}
   <strong>${full_name}</strong>,
   ${party} from ${state}
   is <strong>${age}</strong> years old.
""")

TWEET_BUTTON_HTML = Template("""
<a href="https://twitter.com/share" class="twitter-share-button" data-url="${url}" data-text="Happy birthday, @${twitter_name}, you are ${age} years old!">Tweet</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>
""")


def birthday_html(data_rows, the_date):
    the_year = the_date.year

    # generate the HTML for each list item first
    listcles = ""
    for d in data_rows:
        fullname = d['firstname'] + " "  + d['lastname']
        bth_yr = d['birthdate'][0:4]
        age = the_year - int(bth_yr)

        itemtxt = "<li>"
        itemtxt += LIST_ITEM_HTML.substitute(
                        title=d['title'], full_name=fullname,
                        party=d['party'], state=d['state'],
                        age=age)
        # only add a tweet button if the
        # legislator has a twitter id
        if d['twitter_id']:
            itemtxt += TWEET_BUTTON_HTML.substitute(
                                        twitter_name=d['twitter_id'],
                                        url=d['website'], age=age)
        # finally, we're done with this item
        itemtxt += '</li>'
        # add the string to our big collection string
        listcles += itemtxt

    # now add it to the main html
    h = MAIN_HTML.substitute(date=the_date, member_count=len(data_rows),
                         list_html=listcles)
    return h

