#!/usr/bin/env ruby

input = ARGV[0]

pattern = /[hbtn]/

matches = input.scan(pattern).join

puts matches
