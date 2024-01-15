# ptxttools
A set of text processing utilities written in python.

### Usage
The following shows general usage of the tool.
See command sections for specific examples.

```
python3 ptxttools <command> [command args] [common args]
```

Command can be one of the following:

* [Align](#align-command)
* [CountLines](#count-lines-command)
* [PrefixLines](#prefix-lines-command)
* [Tabulate](#tabulate-command)
* [Version](#version-command)

Command matching is case insensitive and based on partial matches.

Additional info

* See [here](#common-options) for common options.
* See [here](#exit-codes) for exit codes.

--------------------------------------------------------------------------------

## Align Command
Aligns input lines read from stdin based on a particular string found in them.

### Usage
The following example shows usage from the command line.

```
python3 ptxttools align <separator>
```

separator: the string to align the text on.

--------------------------------------------------------------------------------

## Count Lines Command
Counts the number of input lines read from stdin.

### Usage
The following example shows usage from the command line.

```
python3 ptxttools countlines
```

No command options are supported.

--------------------------------------------------------------------------------

## Prefix Lines Command
Prefixes each line of input read from stdin.

### Usage
The following example shows usage from the command line.

```
python3 ptxttools prefix <prefix-text>
```

prefix-text: the text string to prefix each line with.

--------------------------------------------------------------------------------

## Tabulate Command
Aligns text to columns based on a specified delimiter.

### Usage
The following example shows usage from the command line.

```
python3 ptxttools tabulate <delimiter> <complete-lines>
```

delimiter: the text string to use to delimit the columns.
complete-table: set to true to fill in the remaining column header seperators for a markdown table.

--------------------------------------------------------------------------------

## Version Command
Reports the version of the tool.

### Usage
The following example shows usage from the command line.

```
python3 ptxttools version
```

No command options are supported.

--------------------------------------------------------------------------------

## Common Options
No common options are currently supported.

--------------------------------------------------------------------------------

## Exit Codes
The following exit codes can be returned by the application.

|Code|Description            |
|----|-----------------------|
|0   |Success                |
|1   |Command execution error|
|2   |Argument error         |

