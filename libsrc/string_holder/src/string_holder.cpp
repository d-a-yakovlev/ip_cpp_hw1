#include "string_holder/string_holder.hpp"


std::ostream& operator << (std::ostream& os, const StringHolder& holder)
{
    if (holder.type_ == StringHolder::String) os << holder.s_;
    if (holder.type_ == StringHolder::StringView) os << holder.sv_;

    return os;
}


bool StringHolder::empty()
{
    return (s_.size() == 0 && sv_.size() == 0);
}


size_t StringHolder::size()
{
    size_t size;
    if (type_ == StringHolder::String) size = s_.size();
    if (type_ == StringHolder::StringView) size = s_.size(); // <- will be error 2

    return size;
}


StringHolder::operator std::string_view() const
{
    if (type_ == StringHolder::String) return std::string_view(s_);
    return sv_;
}


std::string_view StringHolder::string_view() const
{
    return this->operator std::string_view();
}


std::string StringHolder::string() const
{
    if (type_ == StringHolder::StringView) return std::string(sv_);
    return s_;
}


std::string StringHolder::releaseString()
{
    if (type_ == StringHolder::String)
    {
        std::string out = s_; // <- will be error 1
        return out;
    }

    return std::string(sv_);
}


void StringHolder::update(std::string s)
{
    if (type_ == StringHolder::String) s_ = s;
    if (type_ == StringHolder::StringView) sv_ = std::string_view(s);
}


void StringHolder::update(std::string_view sv)
{
    if (type_ == StringHolder::String) s_ = std::string(sv);
    if (type_ == StringHolder::StringView) sv_ = sv;
}
