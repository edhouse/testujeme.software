
----
## Daily to-do
```dataview
TASK
FROM "Daily"
WHERE !completed
GROUP BY file.link
SORT file.name DESC
```
----

## Lorem ipsum to-do

```dataview
TASK
FROM "Lorem ipsum"
WHERE !completed
GROUP BY file.link
SORT file.name DESC
```