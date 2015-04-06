require 'pry'
require './data_converter'


describe "Given 3 text files as data sources" do
  describe "prepping the data the data" do
    let(:dc) { DataConverter.new }

    it "converts every row to be comma_delimited" do 
      line = 'Smith | Steve | D | M | Red | 3-3-1985'
      line2 = 'Smith Steve D M Red 3-3-1985'
      expect(dc.to_comma_seperated(line)).to eq("Smith,Steve,D,M,Red,3/3/1985\n")
      expect(dc.to_comma_seperated(line2)).to eq("Smith,Steve,D,M,Red,3/3/1985\n")
    end
    
    it "creates a single source of data" do
      data = CSV.parse(dc.all_rows)
      expect(data.length).to eq(9)
    end
    
    it "converts all dates to have mm-dd-YYYY format" do
      row = ['Smith','Steve','NA','M', "3/3/1985", 'Red']
      expect(dc.format_date(row)).to eq('03/03/1985')
    end

    it "adds middle initial if missing" do
      row = ['Smith','Steve','M','Red','3-3-1985']
      expect(dc.middle_name_adjust(row)).to eq(['Smith','Steve','NA','M','Red','3-3-1985'])
    end


  end
end