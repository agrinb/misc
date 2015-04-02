class Award 
  
  attr_accessor :name, :expires_in, :quality, :update_quality
  
  def initialize(name, expires_in, quality)
    @name = name
    @expires_in = expires_in
    @quality = quality
  end

  def increment_award
    if @quality == 80 
      @quality 
    elsif @quality + award_inc_value > 50 
      @quality = 50 
    elsif @quality + award_inc_value < 0
      @quality = 0
    else
      @quality += award_inc_value
    end
  end

  def award_inc_value
    case @name
    when "Blue Distinction Plus"
      80
    when 'NORMAL ITEM' 
      expired? ? -2 :  -1
    when 'Blue First'
      expired? ? 2 : 1
    when 'Blue Compare'
       inc_value_blue_compare
    when 'Blue Star'
      expired? ? -4 : -2
    end
  end

  def inc_value_blue_compare
    if expired?
     -1 * quality
    elsif @expires_in <= 5
      3
    elsif @expires_in <= 10
      2
    else
      1
    end
  end

  def expired?
    @expires_in <= 0
  end

  def update_expiration
    @expires_in -= 1 unless @name == "Blue Distinction Plus"
  end

  def update_award! 
    increment_award
    update_expiration
  end
end

