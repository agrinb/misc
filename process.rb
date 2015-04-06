require 'csv'
require 'pry'
require 'date'

def all_rows
  data = ''
  Dir.glob('data/*.txt') do |file|
    File.open(file) do |in_file|
      in_file.each do |line|
        #convert data to be consistent with other files
        line =  line.gsub('Male', 'M').gsub('Female', 'F')
        data << line.gsub('-', '/').gsub(' ', ',').gsub('|', ',').squeeze(' ') << "\n" #add line breaks between files
      end
    end 
  end
  data = data.squeeze("\n").squeeze(",") #remove consecutive line breaks (\n\n) 
end

def prep_data(data)
  arr = []
  CSV.parse(data) do |row|

    #convert row into array
    #adjust the colum the DOB is in
    if /([0-9]+)\/([0-9]+)\/([0-9]+)/.match(row[-1])
      row[-1], row[-2] = row[-2], row[-1]
    end
    #convert date to mm-dd-yyyy format
    row[-2] = Date.strptime(row[-2], '%m/%d/%Y').strftime('%m/%d/%Y')
    #adjust for missing middle name
    if row.length < 6
      row.insert(2, "NA")
    end
    arr << row
  end
  arr
end






data = prep_data(all_rows)


SurnameIndex = 0
GenderIndex  = 3
DateIndex    = 4

puts "By gender then surname: %s" % data.sort_by.sort_by { |object| [ object[GenderIndex], object[SurnameIndex] ] }.inspect

new_data = data.sort_by.sort_by do |object| 
  Date.strptime(object[DateIndex], '%m/%d/%Y') 
end
puts new_data.inspect
puts "By surname descending: %s" % data.sort_by.sort { |a, b| b[SurnameIndex] <=> a[SurnameIndex] }.inspect




