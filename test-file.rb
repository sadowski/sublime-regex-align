# Begin
{
  :aaa => 'text',
  :bbbbbbbbb      => 'text',
  :cc     => 'text',
  :d                        => 'text'    ,
  :jj => 'text', :kkkk => 'text', :llll => 'text'
  :e => 'text', :f => 'text',
  :hhh => 'text', :iii => 'text',
  :jj => 'text', :kkkk => 'text', :llll => 'text'
}

# Test
{
:a => 0,
:bbbb => 0,
:cc => 0,
:d      => 0  ,
:e => 0, :f => 0,
:hhhh => 0, :iii    => 0,
:jj => 0, :k => 0, :lll => 0,
:j => 0, :kk => 0, :l => 0
}

# Expected
{
  :aaa       => 'text',
  :bbbbbbbbb => 'text',
  :cc        => 'text',
  :d         => 'text',
  :jj        => 'text', :kkkk => 'text', :llll => 'text'
  :e         => 'text' , :f   => 'text',
  :hhh       => 'text', :iii  => 'text',
}