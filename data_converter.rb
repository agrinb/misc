require 'csv'
require 'date'

class DataConverter
  def all_rows
    data = ''
    Dir.glob('data/*.txt') do |file|
      File.open(file) do |in_file|
        in_file.each do |line|
          #convert data to be consistent with other files
          line =  line.gsub('Male', 'M').gsub('Female', 'F')
          data << to_comma_seperated(line)
        end
      end 
    end
    data = data.squeeze("\n") #remove consecutive line breaks (\n\n) 
  end

  def prep_data(data)
    arr = []
    CSV.parse(data) do |row|
      middle_name_adjust(row)
      date_position(row)
      format_date(row)
      arr << row
    end
    arr
  end  
  #convert date to mm-dd-yyyy format
  def format_date(row)
    row[-2] = Date.strptime(row[-2], '%m/%d/%Y').strftime('%m/%d/%Y')
  end
  #adjust the colum the DOB is in
  def date_position(row)
   if /([0-9]+)\/([0-9]+)\/([0-9]+)/.match(row[-1])
      row[-1], row[-2] = row[-2], row[-1]
    end
  end
  #adjust for missing middle name
  def middle_name_adjust(row)
    if row.length < 6
      row.insert(2, "NA")
    end
  end

  def to_comma_seperated(line)
    line.gsub("-", "/").gsub(' ', ',').gsub('|', ',').squeeze(",") << "\n" #add line breaks between files
  end
end

