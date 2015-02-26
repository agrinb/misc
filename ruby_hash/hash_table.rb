require 'pry'

class Hash_me
  attr_accessor :bin_count, :bins

  def initialize
    self.bin_count = 500
    self.bins = Array.new 
  end

  def add(entry)
    binding.pry
    index = bin_for(entry[0])
    self.bins[index] ||= []
    self.bins[index] << entry
  end

  def evl(key)
    index = bin_for(key)
    self.bins[index].detect do |entry|
      entry[0] == key
    end
    entry
  end

  private
  def bin_for(key)
    key.hash % self.bin_count
  end

end