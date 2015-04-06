require 'pry'
require './data_converter'
require 'capybara/rspec'
require 'spec_helper'
require 'feature_spec_helper'


describe "the signin process", :type => :feature do
  it "signs me in" do
    visit '/gender_and_lastname'
    expect(page).to have_content 'Abercrombie'
  end

  # it "signs me in" do
  #   visit '/birth_date'
  #   expect(page).to have_content 'Abercrombie'
  # end

  # it "signs me in" do
  #   visit '/last_name'
  #   expect(page).to have_content 'Abercrombie'
  # end
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
