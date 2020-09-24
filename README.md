# ptxttools
A set of text processing utilities written in python.

### Usage
The following shows general usage of the tool.
See command sections for specific examples.

```
python3 ptxttools <command> [command args] [common args]
```

Command can be one of the following:

* [CountLines](#count-lines-command)
* [Tabulate](#tabulate-command)
* [Version](#version-command)

Command matching is case insensitive and based on partial matches.

Additional info

* See [here](#common-options) for common options.
* See [here](#exit-codes) for exit codes.

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

## Tabulate Command
Aligns text to columns based on a specified delimiter.

### Usage
The following example shows usage from the command line.

```
python3 ptxttools tabulate <delimiter>
```

Delimiter: the text string to use to delimit the columns.

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

