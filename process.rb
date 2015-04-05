require 'csv'
require 'pry'
require 'date'


data = ''
Dir.glob('data/*.txt') do |file|
  File.open(file) do |in_file|
    in_file.each do |line|
      line =  line.gsub('Male', 'M').gsub('Female', 'F')
      data << line.gsub('-', '/').gsub(',', ' ').gsub('|', ' ').squeeze(' ') << "\n"
    end
  end 
end
data = data.squeeze("\n")

arr = []
CSV.parse(data) do |row|
 row = row[0].split(" ")
  unless /([0-9]+)\/([0-9]+)\/([0-9]+)/.match(row[-1])
    row[-1], row[-2] = row[-2], row[-1]
  end
  if row.length < 6
    row.insert(2, nil)
  end
  p row
  arr << row
end 

binding.pry

data = arr

SurnameIndex = 0
GenderIndex  = 3
DateIndex    = 5

puts "By gender then surname: %s" % data.sort_by.sort_by { |object| [ object[GenderIndex], object[SurnameIndex] ] }.inspect

new_data = data.sort_by.sort_by do |object| 
  Date.strptime(object[DateIndex], '%m/%d/%Y') 
end
puts new_data.inspect
puts "By surname descending: %s" % data.sort_by.sort { |a, b| b[SurnameIndex] <=> a[SurnameIndex] }.inspect




