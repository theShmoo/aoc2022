# aoc 2022

[advent of code 2022](https://adventofcode.com/2022)

![day](https://img.shields.io/badge/day%20📅-12-blue)
![stars](https://img.shields.io/badge/stars%20⭐-24-yellow)
![GitHub CI](https://github.com/theShmoo/aoc2022/actions/workflows/workflow.yml/badge.svg)
![coverage](https://img.shields.io/badge/coverage-99%25-success)

## Development

It is written as a python module

## CI/CD

I use github actions for CI/CD.
As I am working alone on this project there is no strict development process.

### Tests

I test the code of the module with 100% line coverage,
or otherwise the pipeline will fail.

## Usage

```man
usage: aoc_2022 [-h] [-d {1,2,3,4,5,6,7,8,9,10,11,12}] [-p {1,2}] [-t] [-e] [-r REPEAT] [-q]

advent of code 2022

options:
  -h, --help            show this help message and exit
  -d {1,2,3,4,5,6,7,8,9,10,11,12}, --day {1,2,3,4,5,6,7,8,9,10,11,12}
                        solve a specific day, if not set solve all days
  -p {1,2}, --part {1,2}
                        solve only for a specific part, if not set solve for all parts
  -t, --timing          add timinig output
  -e, --example         use example data
  -r REPEAT, --repeat REPEAT
                        repeat the execution several times
  -q, --quiet           get minimal output.

by theShmoo
```
