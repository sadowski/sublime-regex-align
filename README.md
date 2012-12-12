sublime-regex-align
=====================

Package for regular expression alignment in sublime text

Installation
===============

Install to your sublime packages directory Packages directory.

Usage
========

Default shortcut key is:
    ctrl+shift+l

Example
==========

Before:
```
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
```
After (Regex: '=>'):
```
{
  :aaa       => 'text',
  :bbbbbbbbb => 'text',
  :cc        => 'text',
  :d         => 'text'    ,
  :jj        => 'text', :kkkk => 'text', :llll => 'text'
  :e         => 'text', :f    => 'text',
  :hhh       => 'text', :iii  => 'text',
  :jj        => 'text', :kkkk => 'text', :llll => 'text'
}
```

