require './server'
require '../data/comma_delimited.txt'
require './data/pipe_delimited'
require './data/space_delimited'

describe "Given 3 text files as data sources" do
  describe "prepping the data the data" do
    it "converts ever row to be space delimited" do 

    end
    
    it "creates a single source of data" do
    #expect 9 rows of data
    end
    
    it "converts all genders to M/F format" do 
    end

    it "converts all dates to have mm-dd-YYYY format" do
    end

    it "adds middle initial if missing" do
    end



    #expect each row of data to have 
    #expect all Gender to be either M or F
    #expect all Dates to follow pattern /([0-9]+)\/([0-9]+)\/([0-9]+)/
  end
    # let(:dom) { Nokogiri::HTML(open('http://intentmedia.com/jobs/')) }

end