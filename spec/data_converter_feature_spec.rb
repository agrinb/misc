require 'pry'
require './data_converter'
require './server'
require 'capybara/rspec'
require 'spec_helper'
require 'feature_spec_helper'

feature "my test" do
    scenario "visit site", :type => :feature do
      visit '/gender_and_lastname'
      expect(first(".list-group-item").text).to have_content("Hingis, Martina, M, F, 04/02/1979, Green")
    end


   scenario "visit site", :type => :feature do
      visit '/birth_date'
      expect(first(".list-group-item").text).to have_content("Abercrombie, Neil, NA, M, 02/13/1943, Tan")
    end

    scenario "visit site", :type => :feature do
      visit '/last_name'
      expect(first(".list-group-item").text).to have_content("Smith, Steve, D, M, 03/03/1985, Red")
    end
end


# get '/gender_and_lastname' do
#   @page_title = "Sorted by gender and last name"
#   @data = data.sort_by.sort_by { |object| [ object[ge_index], object[ln_index] ] }
#   erb :'data/data.html'
# end

# get '/birth_date' do
#   @page_title = "Sorted by birth day"
#   @data = data.sort_by.sort_by do |object| 
#     Date.strptime(object[dt_index], '%m/%d/%Y') 
#   end
#   erb :'data/data.html'
# end
