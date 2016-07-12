using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Retangle
{
   
    class Program
    {
        double length;
        double width;
        public void SetData(){
            length = 4.0;
            width = 3.0;
        }
        public void GetArea(){

            Console.WriteLine("the area is:{0}",length*width);
            
        }
        static void Main(string[] args)
        {
            Program Retan = new Program();
            Retan.SetData();
            Retan.GetArea();
            Console.ReadKey();
     
            
        }
    }
}
