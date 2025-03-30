// Prints out section numbers, short names, and long names.
//
// Typical usage:
//
//   cd draft/source/
//   ../tools/sections std.tex > section_names.txt
//
#include <fstream>
#include <iostream>
#include <regex>
#include <sstream>
#include <string>
#include <vector>

class counter {
public:
  counter()
  : m_data{0}
  , m_annex{false}
  {
  }

  // Bump up the counter at the given depth.
  //
  // For example, 4.7.9 bumped at level 1 becomes 4.8, bumped at level 0 becomes 5.
  void bump(int level)
  {
    m_data.resize(level + 1);
    m_data.back()++;
  }

  // Start a new annex; resets the counter to 'A' the first time it's called,
  // increments as if by bump(0) from there on.
  void annex()
  {
    m_data.resize(1);
    m_data.back() = m_annex ? m_data.back() + 1 : 0;
    m_annex = true;
  }

  typedef std::vector<unsigned> data_t;
  typedef data_t::const_iterator iterator;

  iterator begin() const { return m_data.begin(); }
  iterator end() const { return m_data.end(); }

  bool is_annex() const { return m_annex; }

private:
  data_t m_data;
  bool m_annex;
};

std::ostream& operator<<(std::ostream& os, counter c)
{
  bool first = true;
  for (auto count : c) {
    if (!first) {
      os << '.';
    }
    if (first && c.is_annex()) {
      os << static_cast<char>('A' + count);
    } else {
      os << count;
    }
    first = false;
  }

  return os;
}

void show(counter count, std::string shortname, std::string name)
{
  std::cout << count << ": " << shortname << " - " << name << std::endl;
}

void process(std::string filename, counter& count)
{
  std::cerr << "processing " << filename << std::endl;
  std::ifstream file{filename};
  if (!file) {
    std::ostringstream os;
    os << "Unable to open '" << filename << "' for processing";
    throw std::runtime_error(os.str());
  }

  // We assume below that there is only one of these per source line.
  // In the current draft, they're sometimes followed by comments, so
  // we use regex_search() instead of regex_match() to be robust.
  std::regex include{"^\\\\include\\{(.*)\\}"},
             rSec{"^\\\\rSec([0-9])\\[(.*)\\]\\{(.*)\\}"},
             annex{"^\\\\(inf|norm)annex\\{(.*)\\}\\{(.*)\\}"};

  std::string line;
  while (getline(file, line)) {
    std::smatch results;
    if (regex_search(line, results, include)) {
      auto filename = results.str(1);
      filename += ".tex";
      process(filename, count);
    } else if (regex_search(line, results, rSec)) {
      auto level = results.str(1)[0] - '0';
      auto shortname = results.str(2);
      auto longname = results.str(3);

      count.bump(level);

      show(count, shortname, longname);
    } else if (regex_search(line, results, annex)) {
      auto shortname = results.str(2);
      auto longname = results.str(3);

      count.annex();

      show(count, shortname, longname);
    }
  }
}

void process(std::string filename)
{
  counter count;
  process(filename, count);
}

int main(int argc, char** argv)
{
  if (argc != 2) {
    std::cerr << "Usage: " << argv[0] << " std.tex > output" << std::endl;
    return 1;
  }

  try {
    process(argv[1]);
  } catch (const std::exception& e) {
    std::cerr << e.what() << std::endl;
    return 1;
  }
}
