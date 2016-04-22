public class Quene{
    elementType x;
    Stack S1 =  new Stack();
    Stack S2 = new Stack();
    void push(x)
    {
        if(S2.Is_empty())
        {
            S1.push(x);
        }
         
        else
        {
            for(int i=0; i<S2.count();i++)
            {
                S1.push(S2.pop());
            }
            S1.push(x);
           
        }
        
        
    }
    elementType pop()
    {
        if(S2.Is_empty())
        {
            for(int i=0; i<S1.count()-1; i++ )
            {
                S2.push(S1.pop());
            }
            S1.pop();
        }
        
      else
      {
            S2.pop();
        
      }
        
    }
    
    
}