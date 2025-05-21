# mwdefine

A command-line tool to query the Merriam-Webster Collegiate Dictionary API and print a formatted word definition.

## Usage

```
mwdefine [--api-key <key>] [--raw] <word>
```

- `--api-key`: Your Merriam-Webster API key (or set the `MW_API_KEY` environment variable)
- `--raw`: Print the raw API response

Example:

```
export MW_API_KEY=yourapikey
mwdefine exercise
```

Output:
```
ek-sər-sīz (noun): the act of bringing into play or realizing in action
```

## Build

```
make build
```

## Test

```
make test
```

## Artifact

```
make artifact
```

## Requirements

- Python 3.8+
- Merriam-Webster API key ([get one here](https://dictionaryapi.com/register/index))

