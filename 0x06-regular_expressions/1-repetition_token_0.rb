#!/usr/bin/env ruby

input = ARGV[0]

pattern = /^hb(t{2,5})n$/

if input =~ pattern
  puts input
end
