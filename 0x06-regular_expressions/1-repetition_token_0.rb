#!/usr/bin/env ruby

input = ARGV[0]

pattern = /^hb(t{2,5})n$/

matches = input.scan(pattern).join

puts matches
