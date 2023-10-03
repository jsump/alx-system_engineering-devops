#!/usr/bin/env ruby

input = ARGV[0]

pattern = /^hb?tn$/

if input =~ pattern
  puts input
end
