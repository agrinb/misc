class HashEntry
  def initialize(key, value)
    @key = key
    @value = value
    @entry = [@key, @value]
  end
end