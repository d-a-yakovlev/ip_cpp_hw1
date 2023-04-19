#include <iostream>
#include <sstream>

#define CATCH_CONFIG_MAIN
#include <catch2/catch_test_macros.hpp>
#include <catch2/catch_all.hpp>

#include "string_holder/string_holder.hpp"


TEST_CASE("StringHolder", "[size]")
{
    std::string s = std::string("String for holder");
    std::string_view sv = std::string_view("String view for holder");

	StringHolder sh1 = StringHolder(s);
	REQUIRE( sh1.size() == 17 );
	
    sh1 = StringHolder(std::string());
	REQUIRE( sh1.empty() );

    StringHolder sh2 = StringHolder(sv);
    REQUIRE(sh2.size() == 22); // тест добавляется из-за того, что был исправлен size. 
	
    sh2 = StringHolder(std::string());
	REQUIRE( sh2.empty() );
}


TEST_CASE("StringHolder", "[size_original]")
{
    std::string s = std::string("String for holder");
    std::string_view sv = std::string_view("String view for holder");

	StringHolder sh1 = StringHolder(s);
	REQUIRE( sh1.size() == 17 );
	
    sh1 = StringHolder(std::string());
	REQUIRE( sh1.empty() );

    StringHolder sh2 = StringHolder(sv);
	REQUIRE( sh2.size() == 22 ); // <- will be forgeted 2
	
    sh2 = StringHolder(std::string());
	REQUIRE( sh2.empty() );
}


TEST_CASE("StringHolder", "[data]")
{
    std::string s = std::string("Some data for holder");
    std::string_view sv = std::string_view("Some data for holder");
    {
        StringHolder holder_1(s);
        StringHolder holder_2(sv);

        char* data_1 = holder_1.data();
        const char* data_2 = holder_2.data();

        REQUIRE( std::string(data_2, sv.size() ) == std::string("Some data for holder"));
        REQUIRE( std::string(data_2, sv.size() ) == std::string(data_1, s.size()));

        *(data_1) = 'N';
        REQUIRE( std::string(data_1, s.size() ) == std::string("Nome data for holder"));
        REQUIRE( *(data_2) == 'S' );
    }
    {
        StringHolder holder_1(s);
        StringHolder holder_2(sv);

        const char* data_1 = holder_1.data();
        char* data_2 = holder_2.data();

        REQUIRE( *(data_1) == '\0' ); // guarantee null-terminated by default
        REQUIRE( *(data_2) == '\0' );
    }
}


TEST_CASE("StringHolder", "[operator brackets ]")
{
    std::string s = std::string("Some data for holder");
    std::string_view sv = std::string_view("Some data for holder");
    {
        StringHolder holder_1(s);
        StringHolder holder_2(sv);

        char& elem_1 = holder_1[0];
        REQUIRE(elem_1 == 'S');
        elem_1 = 'N';
        auto elem_2 = holder_2[0].operator const char&();

        REQUIRE(holder_1.string() != s);
        s[0] = 'N';
        REQUIRE(holder_1.string() == s);

        REQUIRE(elem_2 == sv[0]);
       
        REQUIRE(holder_1.string_view() != sv);
        REQUIRE(holder_1.string_view() == std::string_view(s));
    }
}


TEST_CASE("StringHolder", "[operator std::string_view]")
{
    std::string s = "Some str";
    std::string_view sv = s;
    {
        StringHolder holder(sv);
        auto func = [&sv](std::string_view strView)
        {
            REQUIRE(strView == sv);
        };
        func(holder);
    }
    {
        StringHolder holder(s);
        auto func = [&sv](std::string_view strView)
        {
            REQUIRE(strView == sv);
        };
        func(holder);
    }

}


TEST_CASE("StringHolder", "[string_view]")
{
    std::string s = "Some str";
    std::string_view sv = s;
    {
        StringHolder holder(sv);
        REQUIRE(holder.string_view() == sv);
    }
    {
        StringHolder holder(s);
        REQUIRE(holder.string_view() == sv);
    }
}


TEST_CASE("StringHolder", "[string]")
{
    std::string s = "Some str";
    std::string_view sv = s;
    {
        StringHolder holder(sv);
        REQUIRE(holder.string() == s);
    }
    {
        StringHolder holder(s);
        REQUIRE(holder.string() == s);
    }
}


TEST_CASE("StringHolder", "[releaseString]")
{
    std::string s = "Some str";
    std::string_view sv = s;
    {
        StringHolder holder(s);
        std::string gotten_s = holder.releaseString();
        REQUIRE(gotten_s == s);
        REQUIRE(std::string() == holder.string()); // проверка на выполнение move-семантики
    }
    {
        StringHolder holder(sv);
        std::string gotten_s = holder.releaseString(); // in this case releaseString() makes copy
        REQUIRE(gotten_s == s);
        REQUIRE(holder.string() == s); // in this case string() makes interpretation of std::string_view
    }
}


TEST_CASE("StringHolder", "[releaseString_original]")
{
    std::string s = "Some str";
    std::string_view sv = s;
    {
        StringHolder holder(s);
        std::string gotten_s = holder.releaseString();
        REQUIRE(gotten_s == s);
        REQUIRE(holder.string() == std::string()); // <- will be forgeted
    }
    {
        StringHolder holder(sv);
        std::string gotten_s = holder.releaseString(); // in this case releaseString() makes copy
        REQUIRE(gotten_s == s);
        REQUIRE(holder.string() == s); // in this case string() makes interpretation of std::string_view
    }
}


TEST_CASE("StringHolder", "[operator <<]")
{
    std::string s = "Some str";
    std::string_view sv = s;
    {
        StringHolder holder(s);
        std::stringstream os;
        os << holder;
        REQUIRE(os.str() == s);
    }
    {
        StringHolder holder(sv);
        std::stringstream os;
        os << holder;
        REQUIRE(os.str() == s);
    }
}
