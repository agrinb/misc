require 'sinatra'
require "capybara/rspec"
require 'capybara/dsl'


Capybara.app = Sinatra::Application

RSpec.configure do |c|
  #c.include RackSpecHelpers, feature: true
  c.before feature: true do
    self.app = Sinatra::Application
  end

  
  c.include Capybara::DSL, feature: true
  c.include Capybara::RSpecMatchers, feature: true
end

