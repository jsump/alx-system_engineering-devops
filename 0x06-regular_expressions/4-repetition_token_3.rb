#!/usr/bin/env ruby

input = ARGV[0]

pattern = /^hb(t{1,})n$/

if input =~ pattern
  puts input
end
