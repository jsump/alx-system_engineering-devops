#!/usr/bin/env ruby

input = ARGV[0]

pattern = //

matches = input.scan(pattern).join

puts matches
