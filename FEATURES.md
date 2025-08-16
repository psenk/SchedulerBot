# Sith PVM Scheduler Bot

## **Goal:** 

Create a discord bot that helps manage people in Sith regarding PVM experience, time, and availability. 

## **Data Storage:**

Database Tables

1. Name Lookup: UUID, Name
2. TimeZone Lookup: UUID, Timezone
3. Raid Experience: 
   - UUID - Unique User ID
   - Raid - Raid or Content ID
   - Experience - Skill Level

4. Availability:
   - UUID 
   - Day
   - Start Time
   - End Time

Reasoning: By breaking it into these tables, we have the ability to add future tables as well, without having to add many new rows. All times are in EST format, to match the clan.

## **Features:**

### Sign Up For Content:

**Parameters:** 

Content Name: Select Content - Drop Down
Time Zone: Select Current Time - Drop Down
Availability: Select Day with Checkbox - Select Start and End time for each day
Skill Level: Select skill level - Drop Down [Learner, Intermediate, Advanced, Teacher]
<font color=red>What to Learn: For the future - Allow them to select roles they wish to learn</font>

UI: Discord selection menu. Should return a message, add all required content to the table (If no UUID, create one). UUID could be their unique discord name (not server name).

### Content Availability Lookup:

**Parameters:**

Content Name: Select Content that you want to find if other people are available for
Availability: Select Day with Checkbox - Select Start and End time for each day 

	- Bot should look within the table to see if people are available for a whole hour between the start and end time

Minimum Skill Level: Select Skill Level - Drop Down [Learner, Intermediate, Advanced, Teacher]

- Find all people with the desired skillset or better

Discord: Private Showing (either PM or User only Message)

- Table Returned, separated by headings. Learner first, followed by rest.
  - Name - Day - Availabilities