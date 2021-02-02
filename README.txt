This code goes through all the directories and files in the directory given in lines 11 and 13 and fetches all the files with the name "workflow.xml"
upon reading the file, the code looks for a <sh> to parse and inside it looks for a line ending in ".sh". Once found, the code checks for a $ sign at the beggining of the code... If found, this means that the first word is a variable, so the codes look for the definition of the variable and it replaces it.

Example:
Original code:
$file_Path = xyz/abc
<sh>
$file_Path/user/folder/file.sh
</sh>
output:
xyz/abc/user/folder/file.sh
