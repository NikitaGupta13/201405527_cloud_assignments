#include<iostream>
#include<map>
#include<string>
#include<fstream>

using namespace std;

int main(){
	map<string,string> asmmap;
	asmmap["pushl	%ebp"]="pushq	%rbp";
	asmmap[".cfi_def_cfa_offset 8"]=".cfi_def_cfa_offset 16";
	asmmap[".cfi_offset 5, -8"]=".cfi_offset 6, -16";
	asmmap["movl	%esp, %ebp"]="movq	%rsp, %rbp";
	asmmap[".cfi_def_cfa_register 5"]=".cfi_def_cfa_register 6";
	asmmap["andl	$-16, %esp"]="";
	asmmap["subl	$16, %esp"]="";
	asmmap["movl	$.LC0, (%esp)"]="movl	$.LC0, %edi";
	asmmap["leave"]="popq	%rbp";
	asmmap[".cfi_restore 5"]="";
	asmmap[".cfi_def_cfa 4, 4"]=".cfi_def_cfa 7, 8";
	ifstream bitfile("32_bit.s");
	string line;
 	if(bitfile.is_open())
	{
		while(getline(bitfile,line))
		{
			int i;
			for(i=0;i<line.length();i++)
				if(!isspace(line[i]))
					break;
			
			line=line.substr(i,line.length()-i);
			if(asmmap.find(line)!=asmmap.end()){
				if(asmmap[line]!="")
					cout<<asmmap[line]<<endl;
			}
			else
				cout<<line<<endl;
		}
	}
	bitfile.close();	
	return 0;
}
