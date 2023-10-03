#!/usr/bin/env ruby

input = ARGV[0]

pattern = /School/

matches = input.scan(pattern).join

puts matches
