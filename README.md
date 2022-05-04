# Cron Parser Tech Task

Code for the Cron Parser Technical Task

## Useage

Once you've cloned the project, run the following command to parse your Cron into a space seperated output, nicely formatted in a table.

```python3 cronparser.py "<CRON_TO_PARSE>"```

Example:

```python3 cronparser.py "*/15 0 1,15 * 1-5 /usr/bin/find" ```

The following output should be:

```
minute        0 15 30 45
hour          0
day of month  1 5
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   1 2 3 4 5
command       /usr/bin/find
```
