require 'pry'

class Hash_me
  attr_accessor :bin_count, :bins

  def initialize
    self.bin_count = 500
    self.bins = Array.new 
  end


  def add(key, value)
    index = bin_for(key)
    self.bins[index] ||= []
    self.bins[index] << [key, value]
    self
  end

  def evl(key)
    index = bin_for(key)
    bin = self.bins[index].detect do |entry|
      entry[0] == key
    end
    bin[1]
  end

  def merge(entry)
    binding.pry
    entry.bins.each_with_index do |sub,i|
      if self.bins[i] == nil
        self.bins[i] = sub
      else
        self.add(sub[0],sub[1])
      end
    end
    self
  end

  def keys
    keys = []
    self.bins.each do |x|
      unless x == nil
        keys << x[0][0]  
      end
    end
    keys
  end

  def values
    values = []
    self.bins.each do |x|
      unless x == nil
        values << x[0][1]  
      end
    end
    values
  end




  private
  def bin_for(key)
    key.hash % self.bin_count
  end

end