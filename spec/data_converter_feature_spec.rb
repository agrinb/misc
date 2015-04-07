require 'pry'
require_relative "../data_converter.rb"
require_relative "../server.rb"
require 'capybara/rspec'
require 'spec_helper'

#finds the first item expected on every page
feature "browsing sorted lists" do
  scenario "sorted by gender and last name page", :type => :feature do
    visit '/gender_and_lastname'
    expect(first(".list-group-item").text).to have_content("Hingis, Martina, M, F, 04/02/1979, Green")
  end

  scenario "sorted by birthday", :type => :feature do
    visit '/birthday'
    expect(first(".list-group-item").text).to have_content("Abercrombie, Neil, NA, M, 02/13/1943, Tan")
  end

  scenario "sorted last name page", :type => :feature do
    visit '/lastname'
    expect(first(".list-group-item").text).to have_content("Smith, Steve, D, M, 03/03/1985, Red")
  end
end

