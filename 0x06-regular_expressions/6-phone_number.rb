#!/usr/bin/env ruby

input = ARGV[0]

pattern = /^\d{10}$/

matches = input.scan(pattern).join

puts matches
