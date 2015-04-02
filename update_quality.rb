require 'award'

def update_quality(awards)
  awards.each { |award| award.update_award! }
end