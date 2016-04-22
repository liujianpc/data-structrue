public class Stack
{
    elementType x;
    Quene Q1 = new Quene();
    Quene Q2 = new Quene();
    push(x)
    {
        if(!Q1.Is_empty())
        {
            Q1.EnQuene(x);
        }
        
        if(!Q2.Is_empty())
        {
            Q2.EnQuene(x);
        }
    }
    
    elementType pop()
    {
        if(!Q1.Is_empty())
        {
            for(int i = 0; i < Q1.count()-1; i++)
            {
                Q2.EnQuene(Q1.DelQuene());
            }
           return Q1.DelQuene();
        }
        
        if(!Q2.Is_empty())
        {
            for(int i = 0; i < Q2.count(); i++)
            {
                Q1.EnQuene(Q2.DelQuene());
            }
            return Q2.DelQuene();
        }
    }
}