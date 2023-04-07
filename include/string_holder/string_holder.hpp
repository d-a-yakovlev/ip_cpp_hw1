#pragma once

#include <iostream>
#include <string>
#include <string_view>


class StringHolder
{
private:
    enum innerType
    {
        String,
        StringView
    };
    std::string s_ = std::string();
    std::string_view sv_ = std::string_view();
    innerType type_;

public:
    StringHolder() = default;
    StringHolder(std::string s) 
    : s_(s), sv_(std::string_view("\0")), type_(String){}

    StringHolder(std::string_view sv) 
    : sv_(sv), type_(StringView){}

    friend std::ostream& operator << (std::ostream& os, const StringHolder& holder);

    bool empty();
    size_t size();

    operator std::string_view() const;
    std::string_view string_view() const;
    std::string string() const;
    std::string releaseString();

    void update(std::string s);
    void update(std::string_view sv);

    
/*
    BEWARE deep dark magic below!
*/
private:
    friend class resultData;
    struct resultData
    {
        operator char*()
        {
            return holderPtr->s_.data();
        }

        operator const char*()
        {
            return holderPtr->sv_.data();
        }

        operator char&()
        {
            return holderPtr->s_.at(i);
        }


        explicit operator const char& ()
        {
            return holderPtr->sv_.at(i);
        }

        StringHolder* holderPtr;
        size_t i;
    };

public:
    resultData data()
    {
        return resultData{ this, 0 };
    }


    resultData operator [] (size_t i)
    {
        return resultData{ this, i };
    }
/*
    Well thats hack has gotten from 
    https://devblogs.microsoft.com/oldnewthing/20191106-00/?p=103066
*/
};